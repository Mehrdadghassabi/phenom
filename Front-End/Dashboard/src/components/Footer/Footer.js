
import React, { Component } from "react";
import { Container } from "react-bootstrap";

class Footer extends Component {
  render() {
    return (
      <footer className="footer px-0 px-lg-3">
        <Container fluid>
          <nav>
            <ul className="footer-menu">
              <li>
                <a href="#pablo" onClick={(e) => e.preventDefault()}>
                  Home
                </a>
              </li>
              <li>
                <a href="#pablo" onClick={(e) => e.preventDefault()}>
                Rate us
                </a>
              </li>
          
              <li>
                <a href="#pablo" onClick={(e) => e.preventDefault()}>
                 about us
                </a>
              </li>
            </ul>
      
          </nav>
        </Container>
      </footer>
    );
  }
}

export default Footer;
