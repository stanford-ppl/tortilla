const protobuf = require('protobufjs');
const fs = require('fs');

// Load your proto file
protobuf.load("/home/pbeni/Research/tortilla/tortilla-graphviz/proto/tortilla.proto", function(err, root) {
    if (err) {
        throw err;
    }

    // Obtain the message type
    let ProgramGraph = root.lookupType("ProgramGraph");

    // Read the textproto file
    let data = fs.readFileSync('/home/pbeni/Research/tortilla/tortilla-graphviz/proto/visualizeSAM.textproto', 'utf8');

    // Try to decode the message
    try {
        let message = ProgramGraph.decode(Buffer.from(data, 'utf8'));
        console.log("Successfully parsed the message");
    } catch (error) {
        console.error("Error parsing the message: ", error);
    }
});
