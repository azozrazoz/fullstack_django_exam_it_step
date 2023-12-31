import axios from "axios";

const endPoint = process.env.REACT_APP_API_URL || "http://127.0.0.1:8000";

export const getYoutubeTestData = async (setDetails) => {
  await axios.get(`${endPoint}/youtube_test/`)
    .then((res) => {
      setDetails(res.data);
    })
    .catch((err) => {
      console.log(err);
    });
};

export const postYoutubeTestData = async (title, channel) => {
  await axios.post(`${endPoint}/youtube_test/`, {title, channel}, {
    headers: {
      "Content-Type": "application/json"
    }
  })
    .then((response) => {
      console.log(response);
    })
    .catch((error) => {
      console.log(error);
    });
};
