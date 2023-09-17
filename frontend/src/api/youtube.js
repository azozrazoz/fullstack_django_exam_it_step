import axios from "axios";

const endPoint = process.env.REACT_APP_API_URL || "asdf";

export const getYoutubeTestData = (setDetails) => {
  axios
    .get(`${endPoint}/youtube_test`)
    .then((res) => {
      setDetails(res.data);
    })
    .catch((err) => {
      console.log(err);
    });
};

export const postYoutubeTestData = (youtube_test_data) => {
  axios
    .post("/youtube_test", youtube_test_data)
    .then((response) => {
      console.log(response);
    })
    .catch((error) => {
      console.log(error);
    });
};
