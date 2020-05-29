import json
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def getMembers():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

@app.route('/member/<int:member_id>', methods=['GET'])
def retrieveMembers(member_id):
    members = jackson_family.get_all_members()
    return jsonify(members), 400

@app.route('/member', methods=['POST'])
def postMembers():
    members = jackson_family.get_all_members()
    newMember = json.loads(request.data)
    members.append(newMember)
    return jsonify(members), 404

@app.route('/member/<int:member_id>', methods=['DELETE'])
def deleteMembers(member_id):
    members = jackson_family.get_all_members()
    members.pop(member_id)
    return jsonify(members), 200


if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = '3245', debug = True)
