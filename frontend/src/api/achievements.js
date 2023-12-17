import axios from "axios";

const endPoint = process.env.REACT_APP_API_URL || "http://127.0.0.1:8000";

export const getAchievements_data = async (setDetails) => {
  await axios.get(`${endPoint}/achievemnts/`)
    .then((res) => {
    setDetails(res.data);
    console.log(res.data);
    })
    .catch((err) => {
        console.log(err);
    });
};

export const postAchievements_data = async (achievemnts_data) => {
  await axios.post(`${endPoint}/achievemnts/`, achievemnts_data, {
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
