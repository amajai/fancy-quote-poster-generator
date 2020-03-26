import React, { Fragment } from "react";
import logo from "../images/logo.png";
const Header = () => {
  return (
    <Fragment>
      <div class="container">
        <div class="row mt-3">
          <div class="col-4 mx-auto d-flex justify-content-center flex-wrap">
            <img
              id="logo"
              className=" img-fluid"
              src={logo}
              alt="fancy quote poster generator"
            />
            <p className="mb-3 text-center font-weight-bold">
              An app that converts a regular quote into a beautifully generated
              poster.
            </p>
          </div>
        </div>
      </div>

    </Fragment>
  );
};

export default Header;
