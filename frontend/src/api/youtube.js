import axios from "axios";

const endPoint = process.env.DJANGO_APP_API_URL || "asdf";

export const getYoutubeTestData = (setDetails) => {
    console.log(endPoint);
  axios
    .get(`${endPoint}/youtube_test`)
    .then((res) => {
      setDetails(res.data);
    })
    .catch((err) => {
      console.log(err);
    });
};
