import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import UtenteList from "../utente/utentelist";

import axios from "axios";

import { API_URL } from "../constants/index";

class Home extends Component {
    state = {
        students: []
    };

    componentDidMount() {
        this.resetState();
    }

    getUtenti = () => {
        axios.get(API_URL + 'utenti/').then(res => this.setState({ utenti: res.data }));
    };

    resetState = () => {
        this.getUtenti();
    };

    render() {
        return (
            <Container style={{ marginTop: "20px" }}>
                <h5>Auror in servizio</h5>
                <Row>
                    <Col>
                        <UtenteList
                            utenti={this.state.utenti}
                            resetState={this.resetState}
                        />
                    </Col>
                </Row>
            </Container>
        );
    }
}

export default Home;