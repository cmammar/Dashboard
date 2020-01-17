<template>
    <div class="dashboard">
        <div class="container">
            <Navbar></Navbar>
            <br><br><br>

            <main role="main" class="container">
                <div v-if="widgets.length == 0">
                    <br><br><br>
                    <h2>Start by adding widgets <router-link to="AddWidget">here</router-link></h2>
                </div>
                <div v-else>
                    <div class="row" v-for="n_row in max_row">
                        <div class="col-md-4" v-for="wid in 3">
                            <!-- <p>{{n_row*3-4 + wid}}</p> -->
                            <br><br>
                            <span v-if='widgets[n_row*3-4 + wid] && widgets[n_row*3-4 + wid].type == "Trump opinion"'><WidgetTrump></WidgetTrump></span>
                            <span v-if='widgets[n_row*3-4 + wid] && widgets[n_row*3-4 + wid].type == "Weather 1"'><WidgetWeather1 :widget="widgets[n_row*3-4 + wid]"></WidgetWeather1></span>
                            <span v-if='widgets[n_row*3-4 + wid] && widgets[n_row*3-4 + wid].type == "Weather 2"'><WidgetWeather2 :widget="widgets[n_row*3-4 + wid]"></WidgetWeather2></span>
                            <span v-if='widgets[n_row*3-4 + wid] && widgets[n_row*3-4 + wid].type == "Best Movies"'><WidgetBestMovies :widget="widgets[n_row*3-4 + wid]"></WidgetBestMovies></span>
                            <span v-if='widgets[n_row*3-4 + wid] && widgets[n_row*3-4 + wid].type == "Actors Match"'><WidgetActorsMatch :widget="widgets[n_row*3-4 + wid]"></WidgetActorsMatch></span>
                            <span v-if='widgets[n_row*3-4 + wid] && widgets[n_row*3-4 + wid].type == "Time"'><WidgetTime :widget="widgets[n_row*3-4 + wid]"></WidgetTime></span>
                        </div>
                        
                    </div>
                </div>
            </main>
        </div>    
    </div>
</template>

<script>

import Navbar from './Navbar'
import WidgetTrump from '../widgets/WidgetTrump'
import WidgetWeather1 from '../widgets/WidgetWeather1'
import WidgetWeather2 from '../widgets/WidgetWeather2'
import WidgetBestMovies from '../widgets/WidgetBestMovies'
import WidgetActorsMatch from '../widgets/WidgetActorsMatch'
import WidgetTime from '../widgets/WidgetTime'

export default {
    name: "Dashboard",
    components: {
        Navbar,
        WidgetTrump,
        WidgetWeather1,
        WidgetWeather2,
        WidgetBestMovies,
        WidgetActorsMatch,
        WidgetTime,
    },
    data () {
        return {
            widgets: [],
            max_row: 0,
        }
    },
    methods: {
        update_widgets: function() {
            this.$http.get('http://localhost:5005/widgets',
            {headers: {'Authorization': "JWT "+localStorage.access_token}})
                .then((response) => {
                    this.message = "Widgets successfully updated";
                    this.widgets = response.data;
                    this.max_row = Math.round(response.data.length / 3);
                    if (this.widgets.length % 3 > 0)
                        this.max_row++;
                }, (error) => {
                    this.message = "Error";
                });
        }
    },
    beforeMount(){
        this.update_widgets();
    },
}
</script>
<style scoped>
</style>