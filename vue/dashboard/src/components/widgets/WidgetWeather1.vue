<template>
    <div class="WidgetWeather1">
        <div class="container">
            <div class="col-md-12">
                <h3 v-if="error">Loading</h3>
                <div v-else>
                    <h2>{{city}}</h2>
                    <p style="font-size:40px;">{{datas.main.temp}}°C</p>
                    <p>{{datas.weather[0].description}}
                    <br>↑ {{datas.main.temp_max}}°C ↓ {{datas.main.temp_min}}°C</p>
                </div>

            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "WidgetWeather1",
    props: ['widget'],
    data () {
        return {
            city: null,
            datas: null,
            error: true,
        }
    },
    methods: {
        update_widgets: function() {
            this.$http.get('https://api.openweathermap.org/data/2.5/weather?q='+this.city+'&appid=84695e34512f2ca637a048b2c16f97a0&lang=fr&units=metric')
                .then((response) => {
                    this.datas = response.data;
                    this.error = false;
                }, (error) => {
                    this.error = true;
                });
        }
    },
    beforeMount(){
        this.widget.datas = JSON.parse(this.widget.datas);
        this.city = this.widget.datas.city;
        this.update_widgets();
        setInterval(this.update_widgets, this.widget.refresh_time*60*1000);
    },
}
</script>
<style scoped>
</style>