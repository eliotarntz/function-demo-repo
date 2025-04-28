/**
 * HTTP handler for the schema-demo function.
 * Responds with a simple JSON message.
 */
exports.handler = (req, res) => {
  res.status(200).json({message: 'Hello from the schema-demo function!'});
};
