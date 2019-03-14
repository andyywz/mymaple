import { combineReducers } from 'redux';
import { dailiesReducer as dailies } from './components/dailies/dailies.duck';

export default combineReducers({
  dailies
});
