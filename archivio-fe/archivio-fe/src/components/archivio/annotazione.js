import React, { Component, Fragment } from "react";
import Header from "../shared/header";
import { Col, Row } from "reactstrap";
import NavBarHome from "../shared/navbar";

class Annotazione extends Component {
    render() {
        return (
            <Fragment>
                <Header />
                <NavBarHome />
                <Row>
                    <Col>
                        <p>Lista annotazioni per archivio</p>
                    </Col>
                </Row>
            </Fragment>
        );
    }
}

export default Annotazione;