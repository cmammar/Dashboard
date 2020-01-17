<template>
    <div class="ManageWidgets.vue">
        <Navbar></Navbar>
    <br>

    <main role="main" class="container">
        <h1 class="mt-5">Manage Widgets</h1>
        <br><br><br>

        <div class="col-md-8 offset-md-2">
            <p v-if="message">{{message}}</p>
            
            <div class="input-group mb-2" v-for="widget in widgets">
                <button v-if="widget.type == 'Weather 1' || widget.type == 'Weather 2' || widget.type == 'Best Movies' || widget.type == 'Time'" @click="update_widget(widget)" type="button" class="btn btn-success mbtn">Update</button>
                <div class="input-group-prepend">
                    <span class="input-group-text">{{widget.type}}</span>
                </div>
                <input v-model="widget.refresh_time" class="form-control" type="number" placeholder="Refresh timer">
                <input v-model="widget.datas.city" v-if="widget.type == 'Weather 1' || widget.type == 'Weather 2'" type="text" class="form-control inpt" placeholder="City">
                <input v-model="widget.datas.country_code" v-if="widget.type == 'Best Movies'" type="text" class="form-control inpt" placeholder="Country Code">
                <input v-model="widget.datas.city" v-if="widget.type == 'Time'" type="text" class="form-control inpt" placeholder="City">
                <button type="button" class="btn btn-danger mbtn btnl" @click="remove_widget(widget.id)">Delete</button>
            </div>

      </div>
    </main>

    </div>
</template>

<script>
import Navbar from './Navbar'

export default {
    name: "ManageWidgets",
    components: {
        Navbar,
    },
    data () {
        return {
            message: null,
            widgets_names: ["Trump opinion", "Weather 1", "Weather 2", "Best Movies", "Actors Match", "Time"],
            widgets: []
        }
    },
    methods: {
        update_widgets: function() {
            this.$http.get('http://localhost:5005/widgets',
            {headers: {'Authorization': "JWT "+localStorage.access_token}})
                .then((response) => {
                    this.widgets = response.data;

                    for (var i = 0; i < this.widgets.length; i++)
                        this.widgets[i].datas = JSON.parse(this.widgets[i].datas);
                }, (error) => {
                    this.message = "Error";
                });
        },
        remove_widget: function(id) {
            this.$http.delete('http://localhost:5005/widgets/'+id.toString(),
            {headers: {'Authorization': "JWT "+localStorage.access_token}})
                .then((response) => {
                    if (response.data.status == "success") {
                        this.message = response.data.message;
                        this.update_widgets();
                    } else
                        this.message = "Error";
                }, (error) => {
                    this.message = "Error";
                });
        },
        update_widget: function(widget) {
            this.$http.put('http://localhost:5005/widgets/'+widget.id.toString(), {position: widget.position, refresh_timer: widget.refresh_time, datas: JSON.stringify(widget.datas)},
            {headers: {'Authorization': "JWT "+localStorage.access_token}})
                .then((response) => {
                    if (response.data.status == "success") {
                        this.message = response.data.message;
                        this.update_widgets();
                    } else
                        this.message = "Error";
                }, (error) => {
                    this.message = "Error";
                });
        },
    },
    beforeMount(){
        this.update_widgets();
    }
}
</script>
<style scoped>
.inpt, .mbtn {
    margin-right: 7px;
}

.btnl {
    margin-left: 7px;
}

</style>