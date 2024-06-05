import yaml
from quart import Quart, request, jsonify

# Load configuration from YAML file
with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

app = Quart(__name__)

@app.route('/api/data', methods=['POST'])
async def handle_data():
    data = await request.json
    print(data)
    response = "You have sent a request with the text: " + data['data'] + ". Thank you!"
    response = {'received':{'data': response}}
    return jsonify(response)

if __name__ == '__main__':
    port = config['server']['port']
    app.run(port=port)  # Use the port from the YAML configuration
