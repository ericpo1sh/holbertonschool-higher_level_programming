#!/usr/bin/node
// Write a script that computes the number of tasks completed by user id.

const request = require('request');

async function completedTasks (url) {
  request.get(url, (error, response, body) => {
    if (error) console.log(error);
    else if (response.statusCode === 404) console.log(`code: ${response.statusCode}`);
    else if (body) {
      const data = JSON.parse(body);
      const completedTasks = {};
      for (const task of data) {
        if (task.completed) {
          const userId = task.userId;
          if (!completedTasks[userId]) {
            completedTasks[userId] = 1;
          } else {
            completedTasks[userId]++;
          }
        }
      }
      console.log(completedTasks);
    }
  });
}
completedTasks(process.argv[2]);
