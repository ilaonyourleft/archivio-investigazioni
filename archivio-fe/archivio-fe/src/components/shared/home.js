import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import UtenteList from "../utente/utentelist";

import axios from "axios";

import { API_URL } from "../constants/index";
import DropdownSelect from "./dropdown";

class Home extends Component {
    state = {
        utenti: [],
        ruoli: []
    };

    componentDidMount() {
        this.resetState();
    }

    getUtenti = () => {
        axios.get(API_URL + 'utenti/').then(res => this.setState({ utenti: res.data }));
    };

    getRuoli = () => {
        axios.get(API_URL + 'ruoli/').then(res => this.setState({ ruoli: res.data }));
    };

    resetState = () => {
        this.getUtenti();
        this.getRuoli();
    };

    render() {
        return (
            <Container style={{ marginTop: "20px" }}>
                <Row>
                    <Col>
                        <DropdownSelect 
                            items={this.state.ruoli}
                        />
                    </Col>
                </Row>
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