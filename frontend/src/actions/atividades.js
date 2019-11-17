import * as types from '../constants/actionTypes';

export function listaAtividades(settings) {
  return function (dispatch) {
    fetch('http://admin.festivalninja.org/api/atividades').then((response) => {
      response.json().then((atividades) => {
        dispatch({
          type: types.LISTA_ATIVIDADES,
          atividades,
        });
      });
    });
  };
}

export function listaEspacos(settings) {
  return function (dispatch) {
    fetch('http://admin.festivalninja.org/api/espacos').then((response) => {
      return response.json().then((espacos) => {
        return dispatch({
          type: types.LISTA_ESPACOS,
          espacos,
        });
      });
    });
  };
}
