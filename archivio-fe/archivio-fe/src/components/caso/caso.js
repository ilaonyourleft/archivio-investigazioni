import React, { Component, Fragment } from "react";
import { Col, Row } from "reactstrap";
import Header from "../shared/header";
import NavBarHome from "../shared/navbar";

class Caso extends Component {
    render() {
        return (
            <Fragment>
                <Header />
                <NavBarHome />
                <Row>
                    <Col>
                        <p>Lista casi</p>
                    </Col>
                </Row>
            </Fragment>
        );
    }
}

export default Caso;