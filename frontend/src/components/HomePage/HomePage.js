import React from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';

import EscolheDia from '../Agenda/EscolheDia';
import Agenda from '../Agenda/Agenda';
import * as actions from '../../actions/atividades';
import './homePage.scss';
import logofestivalninja from '../../img/logofestivalninja.svg';

class HomePage extends React.Component {
    state = {
        data: '21/11',
    }
    componentDidMount() {
        this.props.actions.listaAtividades();
        this.props.actions.listaEspacos();
    }

  render() {
    const { agenda } = this.props;
    return (
      <div>
        <header className="festival__head">
          <img src={logofestivalninja} alt="Imagem contendo o nome Festival Ninja" className="" />
        </header>

        <section className="festival__program">
          <h2 className="festival__program--title">Programação</h2>
          <div className="festival__program--text">
            <h3>Confira abaixo a </h3>
            <h3>programação completa</h3>
          </div>
        </section>
        <EscolheDia />
        <Agenda agenda={agenda} />

        <article>
          <h2>Quer Participar?</h2>
          <div>
            <h3>Garanta sua vaga</h3>
            <h3>ajudando a financiar o festival</h3>
          </div>
          <a>Garantir vaga</a>

          <p>Quer participar e não pode contribuir?</p>
          <p>Preencha o formulário para receber informações sobre as vagas disponíveis.</p>

          <a>Cadastrar</a>
        </article>

        <footer>
          <a>voltar</a>
        </footer>
      </div>
    );
  }
}

HomePage.propTypes = {
    actions: PropTypes.object.isRequired,
    agenda: PropTypes.object,
};

HomePage.defaultProps = {
    agenda: new Agenda([], []),
};

function mapStateToProps(state) {
    return {
        agenda: state.agenda.agenda,
    };
}

function mapDispatchToProps(dispatch) {
  return {
    actions: bindActionCreators(actions, dispatch)
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(HomePage);
