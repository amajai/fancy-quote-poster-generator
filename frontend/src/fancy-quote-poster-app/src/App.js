import React, { Component } from "react";
import axios from "axios";
import download from "downloadjs";
import Header from "./components/Header";
import TemplateSelector from "./components/TemplateSelector";
import OutputField from "./components/OutputField";
import InputField from "./components/InputField";

class App extends Component {
  state = {
    loading: false,
    imgData: "",
    uploadedImgData: "",
    template: "model-1",
    posterPreview: true,
    quoteText: "",
    quoteSource: "",
    quoteOwner: "",
    logoImg: "",
    websiteDomain: "",
    socialNetwork1: ""
  };

  templateOptionHandler = e => {
    this.setState({ template: e.target.value });
  };

  encodeImageToBg = () => {
    var filesSelected = document.getElementById("ImageToBg").files;
    if (filesSelected.length > 0) {
      var fileToLoad = filesSelected[0];
      var fileReader = new FileReader();
      fileReader.onload = fileLoadedEvent => {
        var srcData = fileLoadedEvent.target.result.split(",").pop(); // <--- data: base64
        this.setState({ uploadedImgData: srcData });
      };
      fileReader.readAsDataURL(fileToLoad);
    }
  };

  encodeImageToLogo = () => {
    var filesSelected = document.getElementById("ImageToLogo").files;
    if (filesSelected.length > 0) {
      var fileToLoad = filesSelected[0];
      var fileReader = new FileReader();
      fileReader.onload = fileLoadedEvent => {
        var srcData = fileLoadedEvent.target.result.split(",").pop(); // data: base64
        this.setState({ logoImg: srcData });
      };
      fileReader.readAsDataURL(fileToLoad);
    }
  };

  onChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  onSubmit = e => {
    e.preventDefault();
    this.sendData();
    this.setState({ imgData: "" });
  };

  sendData = async () => {
    const {
      uploadedImgData,
      template,
      quoteText,
      quoteSource,
      quoteOwner,
      logoImg,
      websiteDomain
    } = this.state;
    this.setState({ posterPreview: false, loading: true });
    await axios({
      method: "POST",
      url: `/download-img/${template}`,
      baseURL: "https://fancy-quote-poster-app.herokuapp.com",
      headers: { "content-type": "application/json" },
      data: {
        uploadedImgData: uploadedImgData,
        quoteText: quoteText,
        quoteSource: quoteSource,
        quoteOwner: quoteOwner,
        logoImg: logoImg,
        websiteDomain: websiteDomain
      }
    })
      .then(response => {
        const imgData = response.data.imgData;
        console.log(response.data);
        this.setState({ imgData });
        return response.data;
      })
      .catch(error => {
        console.log(error);
      });
    this.setState({ loading: false });
  };

  downloadImg = () => {
    download(
      `data:image/png;base64, ${this.state.imgData}`,
      "poster-img.png",
      "image/png"
    );
  };

  render() {
    return (
      <div className="container">
        <Header />
        <TemplateSelector
          modelType={this.state.template}
          templateOptionHandler={this.templateOptionHandler}
        />
        <div className="row" id="base">
          <OutputField
            imgData={this.state.imgData}
            downloadImg={this.downloadImg}
            posterPreview={this.state.posterPreview}
            loading={this.state.loading}
          />
          <InputField
            modelType={this.state.template}
            submit={this.onSubmit}
            onChange={this.onChange}
            quoteText={this.state.quoteText}
            quoteSource={this.state.quoteSource}
            quoteOwner={this.state.quoteOwner}
            websiteDomain={this.state.websiteDomain}
            encodeImageToBg={this.encodeImageToBg}
            encodeImageToLogo={this.encodeImageToLogo}   
          />

        </div>
      </div>
    );
  }
}

export default App;
