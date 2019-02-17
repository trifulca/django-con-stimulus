import { Controller } from "stimulus"

export default class extends Controller {
  connect() {
    console.log("Hello, este demo Stimulus!", this.element)
  }
}
