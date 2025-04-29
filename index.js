exports.helloHttp = (req, res) => {
  const msg = req.query.message || req.body.message || 'Hello World!';
  res.status(200).send(`Function received: ${msg}`);
};

