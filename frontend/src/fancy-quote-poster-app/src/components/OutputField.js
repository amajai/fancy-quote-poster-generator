import React from "react";

const OutputField = ({ imgData, downloadImg, posterPreview, loading }) => {
  return (
    <div className="border border-secondary rounded col-11 col-md-4 order-md-2 mx-2 ">
      {imgData && (
        <img
          draggable="false"
          width="250"
          className="rounded mx-auto d-block mt-3 img-fluid unselectable"
          alt="preview-img"
          src={`data:image/png;base64, ${imgData}`}
        />
      )}
      {imgData && (
        <button
          className="btn btn-success mt-3 btn-lg btn-block"
          onClick={downloadImg}
        >
          Download!
        </button>
      )}
      {posterPreview && (
        <div
          style={{ minHeight: "350px" }}
          className="d-flex align-items-center justify-content-center "
        >
          <div className="text-center container d-flex flex-column align-items-center">
            <div
              style={{ height: "200px", width: "200px" }}
              className="border border-primary rounded mb-3 d-flex align-items-center justify-content-center"
            >
              Image Preview
            </div>
            <h5>
              Select a model and fill in the required fields to generate a
              poster.
            </h5>
          </div>
        </div>
      )}

      {loading && (
        <div
          style={{ minHeight: "350px" }}
          className="d-flex align-items-center justify-content-center "
        >
          <div className="text-center">
            <div className="spinner-border" role="status">
              <span className="sr-only">Loading...</span>
            </div>
            <p>Generating poster...</p>
          </div>
        </div>
      )}
    </div>
  );
};

export default OutputField;
