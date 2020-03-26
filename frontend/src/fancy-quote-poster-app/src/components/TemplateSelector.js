import React from "react";

const TemplateSelector = ({ modelType, templateOptionHandler }) => {
  return (
    <div className="row container mb-3">
      <div className="col-md-4">
        <h4>Select a model template: </h4>
      </div>
      <div className="col-md-3 d-flex">
        <select
          className="custom-select"
          value={modelType}
          onChange={templateOptionHandler}
        >
          <option value="model-1">Model 1</option>
          <option value="model-2">Model 2</option>
          <option value="model-3">Model 3</option>
        </select>
      </div>
    </div>
  );
};

export default TemplateSelector;
