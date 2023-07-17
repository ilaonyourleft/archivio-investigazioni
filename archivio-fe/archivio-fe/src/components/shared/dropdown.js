import React, { Component } from 'react';
import { Dropdown, DropdownToggle, DropdownMenu, DropdownItem } from 'reactstrap';

class DropdownSelect extends Component {
    constructor(props) {
        super(props);

        this.toggle = this.toggle.bind(this);
        this.state = {
            dropdownOpen: false
        };
    }

    toggle() {
        this.setState(prevState => ({
            dropdownOpen: !prevState.dropdownOpen
        }));
    }

    render() {
        const items = this.props.items;
        return (
            <Dropdown isOpen={this.state.dropdownOpen} toggle={this.toggle} style={{ marginTop: "20px" }}>
                <DropdownToggle caret>
                    Seleziona un'opzione
                </DropdownToggle>
                <DropdownMenu>
                    {!items || items.length <= 0 ? (
                        <b>Nessuna opzione disponibile</b>
                    ) : (
                        items.map(item => (
                            <DropdownItem key={item.pk}>{item.nome}</DropdownItem>
                        ))
                    )}
                </DropdownMenu>
            </Dropdown>
        );
    }
}

export default DropdownSelect;