import React, { Component, Fragment } from "react";
import { Table } from "reactstrap";

class UtenteList extends Component {
    render() {
        const utenti = this.props.utenti;
        return (
            <Table dark hover responsive>
                <thead>
                    <tr>
                        <th>Nome</th>
                        <th>Cognome</th>
                        <th>Username</th>
                    </tr>
                </thead>
                <tbody>
                    {!utenti || utenti.length <= 0 ? (
                        <tr>
                            <td colSpan="6" align="center">
                                <b>Nessun utente per il ruolo selezionato</b>
                            </td>
                        </tr>
                    ) : (
                        utenti.map(utente => (
                            <tr key={utente.pk}>
                                <td>{utente.nome}</td>
                                <td>{utente.cognome}</td>
                                <td>{utente.username}</td>
                            </tr>
                        ))
                    )}
                </tbody>
            </Table>
        );
    }
}

export default UtenteList;