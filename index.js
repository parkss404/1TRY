const express = require("express");
const app = express();
const logger = require("morgan");
const bodyParser = require("body-parser");

const apiRouter = express.Router();

app.use(logger("dev", {}));
app.use(bodyParser.json());
app.use(
  bodyParser.urlencoded({
    extended: true,
  })
);

app.use("/api", apiRouter);

apiRouter.post("/sayHello", function (req, res) {
  const responseBody = {
    version: "2.0",
    template: {
      outputs: [
        {
          simpleText: {
            text: "나는 라면이 좋다.",
          },
        },
      ],
    },
  };

  res.status(200).send(responseBody);
});

apiRouter.post("/ramen", function (req, res) {
  console.log(req.body);

  const responseBody = {
    version: "2.0",
    template: {
      outputs: [
        {
          simpleImage: {
            imageUrl:
              "https://dimg.donga.com/a/500/0/90/5/ugc/CDB/29STREET/Article/60/66/bc/e1/6066bce10edbd2738275.jpg",
            altText: "라면 이미지",
          },
        },
      ],
    },
  };

  res.status(200).send(responseBody);
});

app.listen(3000, function () {
  console.log("Example skill server listening on port 3000!");
});
