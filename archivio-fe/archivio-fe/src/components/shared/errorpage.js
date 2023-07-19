import React from "react";
import { Col, Container, Row } from "reactstrap";
import { useRouteError } from "react-router-dom";

export default function ErrorPage() {
    const error = useRouteError();
    console.error(error);

    return (
        <Container style={{ marginTop: "20px" }}>
            <Row>
                <Col>
                    <h1>Oops!</h1>
                    <p>Sorry, an unexpected error has occurred.</p>
                    <p>
                        <i>{error.statusText || error.message}</i>
                    </p>
                </Col>
            </Row>
        </Container>
    );
}