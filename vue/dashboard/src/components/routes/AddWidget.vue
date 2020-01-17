<template>
    <div class="AddWidget">
        <Navbar></Navbar>
    <br>

    <main role="main" class="container">
      <h1 class="mt-5">Adding a Widget</h1>
      <br><br><br>

      <div class="col-md-8 offset-md-2">
      <p v-if="message">{{message}}</p>
      <form>
        <div class="form-group row">
            <!-- <label class="my-1 mr-2">Widget</label> -->
            <!-- <label for="example-number-input" class="col-2 col-form-label">Widget</label> -->
            <div class="col-md-8 offset-md-2">
                <select v-model="choice" name="choice" class="custom-select my-1 mr-sm-2" id="inlineFormCustomSelectPref">
                    <option v-for="(widget, index) in widgets" :value="index">{{widget}}</option>
                </select>
            </div>
        </div>

        <div v-if="choice == 1 || choice == 2 || choice == 5" class="form-group row">
            <label for="inputEmail3" class="col-sm-2 col-form-label">City</label>
            <div class="col-sm-8">
            <input v-model="city" class="form-control" id="inputEmail3" placeholder="Paris">
            </div>
        </div>

        <div v-if="choice == 3" class="form-group row">
            <label for="inputEmail3" class="col-sm-2 col-form-label">Country code</label>
            <div class="col-sm-8">
            <input v-model="country_code" class="form-control" id="inputEmail3" placeholder="FR, US ...">
            </div>
        </div>
        
        <div class="form-group row">
            <label for="example-number-input" class="col-2 col-form-label">Refresh timer (min)</label>
            <div class="col-sm-8">
                <input v-model="refresh_timer" class="form-control" type="number" id="example-number-input">
            </div>
        </div>

        </form>
        <div class="form-group row">
            <div class="col-sm-10">
                <button @click="send()" class="btn btn-primary">Add</button>
            </div>
        </div>
      </div>
    </main>

    </div>
</template>

<script>
import Navbar from './Navbar'

export default {
    name: "AddWidget",
    components: {
        Navbar,
    },
    data () {
        return {
            message: null,
            widgets: ["Trump opinion", "Weather 1", "Weather 2", "Best Movies", "Actors Match", "Time"],
            choice: 0,
            refresh_timer: 5,
            city: null,
            country_code: null,
            datas: {}
        }
    },
    methods: {
        send: function() {
            if (this.choice == 1 || this.choice == 2 || this.choice == 5)
                this.datas['city'] = this.city;
            if (this.choice == 3)
                this.datas['country_code'] = this.country_code;
            this.$http.post('http://localhost:5005/widgets', {
                position: -1,
                refresh_timer: this.refresh_timer,
                type: this.widgets[this.choice],
                datas: JSON.stringify(this.datas)
            },
            {headers: {'Authorization': "JWT "+localStorage.access_token}})
                .then((response) => {
                    this.message = "Widget successfully added";
                }, (error) => {
                    this.message = "Error";
                });
        }
    }
}
</script>
<style scoped>
</style>