#!/usr/bin/node
const request = require('request');

const id = process.argv[2];

if (parseInt(episodeId) < 8) {
  const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

  request(url, (err, res, body) => {
    if (err) {
      return console.log(err);
    }
    console.log(JSON.parse(body).title);
  });
