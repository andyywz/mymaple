import axios from 'axios';

const defaultState = {
  data: [],
  loading: false,
  loaded: false
}

// Reducer
export default (state = defaultState, action = {}) => {
  switch (action.type) {
    case GET_DAILIES:
      return {
        ...state,
        loading: true
      };
    case GET_DAILIES_SUCCESS:
      return {
        ...state,
        data: action.payload
      };
    default:
      return state;
  }
}

// Actions
export const GET_DAILIES = 'GET_DAILIES';
export const GET_DAILIES_SUCCESS = 'GET_DAILIES_SUCCESS';

// Action Creators
export const getDailiesRequest = () => ({
  type: GET_DAILIES
});

export const getDailiesSuccess = (payload) => ({
  type: GET_DAILIES_SUCCESS,
  payload
});

// Thunk
export const getDailies = () => dispatch => {
  dispatch({ type: GET_DAILIES });
  axios
    .get('/api/dailies/')
    .then(res => {
      dispatch({
        type: GET_DAILIES_SUCCESS,
        payload: res.data
      });
    })
    .catch(err => console.log(err));
}
