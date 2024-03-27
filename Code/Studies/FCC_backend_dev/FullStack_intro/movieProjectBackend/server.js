import express from "express";
import cors from "cors";
import reviews from "./api/reviews.route.js";

const app = express();

app.use(cors());
app.use(express.json());

// best practices to version the api
// reviews is the route
app.use("/api/v1/reviews", reviews);

// req is request res is response
app.use("*", (req, res) => res.status(404).json({ error: "not found" }));

export default app;
