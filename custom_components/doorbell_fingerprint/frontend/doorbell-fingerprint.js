class DoorbellFingerprint extends HTMLElement {
  constructor() {
    super();
    const template = document.getElementById("doorbell-fingerprint-template");
    const shadowRoot = this.attachShadow({ mode: "open" });
    shadowRoot.appendChild(template.content.cloneNode(true));
  }
}

customElements.define("doorbell-fingerprint", DoorbellFingerprint);
