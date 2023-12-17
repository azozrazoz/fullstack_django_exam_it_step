import axios from "axios";

const endPoint = process.env.REACT_APP_API_URL || "http://127.0.0.1:8000";

export const getLessons_data = async (setDetails) => {
  await axios.get(`${endPoint}/lessons/`)
    .then((res) => {
    setDetails(res.data);
    console.log(res.data);
    })
    .catch((err) => {
        console.log(err);
    });
};

export const postLessons_data = async (lessons_data) => {
  await axios.post(`${endPoint}/lessons/`, lessons_data, {
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
