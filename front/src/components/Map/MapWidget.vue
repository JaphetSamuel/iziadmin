<template>
    <a-card >
        <a-card-meta>
            <template #title>
                <a-row>
                    <a-col :span="18">
                        <h4>Carte</h4>
                    </a-col>
                    <a-col v-if="resizable" :span="6" align="end">
                        <a-icon type="fullscreen"/>
                    </a-col>
                </a-row>
            </template>
        </a-card-meta>
        <l-map style="height: 80vh;" :zoom="zoom" :center="center">
            <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
            <l-polyline v-for="polygone, k in polygon" :key="k" color="blue" :lat-lngs="polygone">
                <l-popup > <span> Yay I was opened by {{polygone}}</span></l-popup>
            </l-polyline>
        </l-map>
    </a-card>
</template>
<script >
import L from 'leaflet';
import { LMap, LTileLayer, LMarker, LPolyline, LPopup } from 'vue2-leaflet';
import Axios from 'axios'

function getAllTrajet(){
    return Axios.get("https://stormy-tor-92609.herokuapp.com/client/commande/")
}


export default {
    props:{
        height:"80vh",
        resizable:false
    },
    components:{
        LMap, LTileLayer, LMarker, LPolyline, LPopup
    },
    data () {
    return {
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      attribution:
        '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      zoom: 12,
      center: [5.326607, -4.022139],
      markerLatLng: [51.504, -0.159],
      polygones:[],
      courses:[]
    }
  },
  computed:{
      polygon:function(){
          let result = this.polygones.map((e)=>{
              return e.map((m)=>m.reverse())
          })
          console.log(result);
          return result
      }
  },
  beforeMount:async function(){
      var r = await getAllTrajet()
      let orders = r.data
      orders.forEach(element => {
        //   console.log(element);
        element.polygone
          this.courses.push({
            client_id: element.client.id,
            statut:element.statut,
            prix:element.prix,
            distance:element.trajet.total_distance,
            from : element.trajet.dep_name,
            polygone:element.trajet.polygone
          })
          this.polygones.push(element.trajet.polygone)
      });
      console.log(this.courses);
  },
}
</script>