import axios from "axios";

const endPoint = process.env.REACT_APP_API_URL || "http://127.0.0.1:8000";

export const getStudent_data = async (setDetails) => {
  await axios.get(`${endPoint}/users/`)
    .then((res) => {
    setDetails(res.data);
    console.log(res.data);
    })
    .catch((err) => {
        console.log(err);
    });
};

export const postStudent_data = async (student_data) => {
  await axios.post(`${endPoint}/users/`, student_data, {
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
