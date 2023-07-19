import React, { Component, Fragment } from "react";
import { Col, Row } from "reactstrap";
import Header from "../shared/header";
import NavBarHome from "../shared/navbar";

class Archivio extends Component {
    render() {
        return (
            <Fragment>
                <Header />
                <NavBarHome />
                <Row>
                    <Col>
                        <p>Lista archivi</p>
                    </Col>
                </Row>
            </Fragment>
        );
    }
}

export default Archivio;