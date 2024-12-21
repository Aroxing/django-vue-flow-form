import { createApp } from 'vue'
import App from './App.vue'
import { FlowForm } from '@ditdot-dev/vue-flow-form'
import '@ditdot-dev/vue-flow-form/dist/vue-flow-form.css'

const app = createApp(App)
app.component('FlowForm', FlowForm)
app.mount('#app') 