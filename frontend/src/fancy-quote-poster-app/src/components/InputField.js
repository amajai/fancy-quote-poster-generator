import React from "react";

const InputField = ({
  modelType,
  submit,
  onChange,
  quoteText,
  quoteSource,
  quoteOwner,
  websiteDomain,
  encodeImageToBg,
  encodeImageToLogo
}) => {
  return (
    <div className="border border-secondary rounded col-11 col-md-7 order-md-1 mx-2 p-2">
      <h3 className="m-3">{modelType.toUpperCase()} TEMPLATE</h3>
      <form onSubmit={submit} className="container">
        {modelType === "model-1" && (
          <div>
            <div className="form-row">
              <div className="form-group col-md-12">
                <label htmlFor="quoteText">Add quote</label>
                <input
                  className="form-control form-control-sm"
                  value={quoteText}
                  onChange={onChange}
                  placeholder=""
                  type="text"
                  name="quoteText"
                  id="quoteText"
                />
              </div>
            </div>
            <div className="form-row">
              <div className="form-group col-md-6">
                <label htmlFor="quoteOwner">Add quote owner</label>
                <input
                  className="form-control form-control-sm"
                  value={quoteOwner}
                  onChange={onChange}
                  placeholder=""
                  type="text"
                  name="quoteOwner"
                  id="quoteOwner"
                />
              </div>
              <div className="form-group col-md-6">
                <label htmlFor="websiteDomain">Add web domain</label>
                <input
                  className="form-control form-control-sm"
                  value={websiteDomain}
                  onChange={onChange}
                  placeholder=""
                  type="text"
                  name="websiteDomain"
                  id="websiteDomain"
                />
              </div>
            </div>
          </div>
        )}
        {modelType === "model-2" && (
          <div>
            <div className="form-row">
              <div className="form-group col-md-6">
                <label htmlFor="quoteText">Add quote</label>
                <input
                  className="form-control form-control-sm"
                  value={quoteText}
                  onChange={onChange}
                  placeholder=""
                  type="text"
                  name="quoteText"
                  id="quoteText"
                />
              </div>

              <div className="form-group col-md-6">
                <label htmlFor="quoteSource">Add quote source</label>
                <input
                  className="form-control form-control-sm"
                  value={quoteSource}
                  onChange={onChange}
                  placeholder=""
                  type="text"
                  name="quoteSource"
                  id="quoteSource"
                />
              </div>
            </div>
            <div className="form-row">
              <div className="form-group col-md-6">
                <label htmlFor="quoteOwner">Add quote owner</label>
                <input
                  className="form-control form-control-sm"
                  value={quoteOwner}
                  onChange={onChange}
                  placeholder=""
                  type="text"
                  name="quoteOwner"
                  id="quoteOwner"
                />
              </div>
              <div className="form-group col-md-6">
                <label htmlFor="websiteDomain">Add web domain</label>
                <input
                  className="form-control form-control-sm"
                  value={websiteDomain}
                  onChange={onChange}
                  placeholder=""
                  type="text"
                  name="websiteDomain"
                  id="websiteDomain"
                />
              </div>
            </div>
          </div>
        )}
        {modelType === "model-3" && (
          <div>
            <div className="form-row">
              <div className="form-group col-md-12">
                <label htmlFor="quoteText">Add quote</label>
                <input
                  className="form-control form-control-sm"
                  value={quoteText}
                  onChange={onChange}
                  placeholder=""
                  type="text"
                  name="quoteText"
                  id="quoteText"
                />
              </div>
            </div>
            <div className="form-row">
              <div className="form-group col-md-12">
                <label htmlFor="quoteOwner">Add quote owner</label>
                <input
                  className="form-control form-control-sm"
                  value={quoteOwner}
                  onChange={onChange}
                  placeholder=""
                  type="text"
                  name="quoteOwner"
                  id="quoteOwner"
                />
              </div>
            </div>
          </div>
        )}
        <div className="form-row">
          <div className="form-group col-md-6">
            <label>
              Add image background.
              <i class="text-danger">
                {" "}
                Square aspect ratio image is recommended.
              </i>
            </label>
            <input
              id="ImageToBg"
              type="file"
              onChange={encodeImageToBg}
              required
            />
          </div>
          <div className="form-group col-md-6">
            <label>
              Add logo.{" "}
              <i class="text-danger">
                Square aspect ratio image is recommended.
              </i>
            </label>
            <br />
            <input id="ImageToLogo" type="file" onChange={encodeImageToLogo} />
          </div>
        </div>
        <button className="btn btn-primary btn-lg btn-block" type="submit">
          Submit
        </button>
      </form>
    </div>
  );
};

export default InputField;
