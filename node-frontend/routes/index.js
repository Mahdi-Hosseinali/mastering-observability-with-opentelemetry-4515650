const express = require("express");

const router = express.Router();
const axios = require("axios");

const votes = {
  spaces: [],
  tabs: [],
};

module.exports = () => {
  router.get("/", async (req, res, next) => {
    try {
      if (
        req.query.choice &&
        req.query.choice !== "spaces" &&
        req.query.choice !== "tabs" &&
        req.query.choice !== "clear"
      ) {
        return res.status(400).end();
      }

      const GATEWAY_URL = process.env.GATEWAY_URL || 'http://127.0.0.1:3001';
      console.log(`BACKEND_URL: ${GATEWAY_URL}`);
      const { data } = await axios.get(
        `${GATEWAY_URL}?choice=${req.query.choice}`
      );
      return res.render("index", data);
    } catch (err) {
      return next(err);
    }
  });

  return router;
};
