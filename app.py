# app.py

from flask import Flask, jsonify, request, render_template
from uuid import uuid4
from blockchain import Blockchain

app = Flask(__name__)
node_id = str(uuid4()).replace('-', '')
blockchain = Blockchain()


@app.route('/')
def index():
    return render_template('index.html', chain=blockchain.chain, peers=list(blockchain.nodes))


@app.route('/mine', methods=['GET'])
def mine():
    last_proof = blockchain.last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    blockchain.new_transaction(sender="0", recipient=node_id, amount=1)

    previous_hash = blockchain.hash(blockchain.last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': 'New Block Forged',
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }

    return jsonify(response), 200


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()

    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400

    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])
    return jsonify({'message': f'Transaction will be added to Block {index}'})



@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200


@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    values = request.get_json()

    if not values or 'nodes' not in values:
        return "Error: Please supply a valid list of nodes", 400

    nodes = values['nodes']
    for node in nodes:
        blockchain.register_node(node)

    return jsonify({'message': 'New nodes have been added', 'total_nodes': list(blockchain.nodes)}), 201



@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    replaced = blockchain.resolve_conflicts()

    if replaced:
        response = {
            'message': 'Our chain was replaced',
            'new_chain': blockchain.chain
        }
    else:
        response = {
            'message': 'Our chain is authoritative',
            'chain': blockchain.chain
        }

    return jsonify(response), 200


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='Port to run the node on')
    args = parser.parse_args()

    app.run(host='0.0.0.0', port=args.port, debug=True)
