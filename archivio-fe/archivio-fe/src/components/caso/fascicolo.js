import React, { Component, Fragment } from "react";
import Header from "../shared/header";
import { Row, Col } from "reactstrap";
import NavBarHome from "../shared/navbar";

class Fascicolo extends Component {
    render() {
        return (
            <Fragment>
                <Header />
                <NavBarHome />
                <Row>
                    <Col>
                        <p>Lista fascicoli per caso</p>
                    </Col>
                </Row>
            </Fragment>
        );
    }
}

export default Fascicolo;