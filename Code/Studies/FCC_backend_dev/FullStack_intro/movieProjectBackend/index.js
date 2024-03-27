import "dotenv/config";
import app from "./server.js";
import mongodb from "mongodb";
// import ReviewsDAO from "./dao/reviewsDAO.js";

const MongoClient = mongodb.MongoClient;
const mongo_username = process.env.MONGO_USERNAME;
const mongo_password = process.env.MONGO_PASSWORD;
const uri = `mongodb+srv://${mongo_username}:${mongo_password}@cluster0.ozyh7zd.mongodb.net/`;
const port = 8000; //27017

MongoClient.connect(uri, {
  maxPoolSize: 50,
  wtimeoutMS: 2500,
  //   useNewUrlParser: true,
})
  .catch((err) => {
    console.error(err.stack);
    process.exit(1);
  })
  .then(async (client) => {
    app.listen(port, () => {
      console.log(`listening on port ${port}`);
    });
  });
