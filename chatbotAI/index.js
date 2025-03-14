const express = require('express');
const bodyParser = require('body-parser');
const dialogflow = require('@google-cloud/dialogflow');
const cors = require('cors');
const path = require('path');

const app = express();
app.use(bodyParser.json());
app.use(cors());

const projectId = 'mychatbot-mlui';
const sessionId = '123456';
const keyFilePath = path.join(__dirname, 'dialogflow_key.json');

async function getDialogflowResponse(message) {
    const sessionClient = new dialogflow.SessionsClient({ keyFilename: keyFilePath });
    const sessionPath = sessionClient.projectAgentSessionPath(projectId, sessionId);

    const request = {
        session: sessionPath,
        queryInput: {
            text: {
                text: message,
                languageCode: 'en',
            },
        },
    };

    const responses = await sessionClient.detectIntent(request);
    const result = responses[0].queryResult;
    return result.fulfillmentText;
}

app.post('/dialogflow', async (req, res) => {
    try {
        const userMessage = req.body.message;
        const botResponse = await getDialogflowResponse(userMessage);
        res.json({ reply: botResponse });
    } catch (error) {
        res.status(500).json({ error: 'Error processing request' });
    }
});

app.listen(5000, () => {
    console.log('Dialogflow server running on port 5000');
});
