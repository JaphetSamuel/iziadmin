<template>
    <main style="background-color:white;padding:10px;">
        <a-page-header title="Nouveau service" @back="back">
            <template #extra>
                <a-radio-group v-model="service.categorie_id">
                    <a-radio-button value="share"> Partager </a-radio-button>
                    <a-radio-button value="eco"> Eco </a-radio-button>
                    <a-radio-button value="luxe"> Confort </a-radio-button>
                </a-radio-group>
            </template>
        </a-page-header>
            <a-row type="flex"  :gutter="[16,16]">
            <a-col :span="8">
                <a-input  placeholder="Nom" v-model="service.name"/>
            </a-col>
            <a-col :span="8">
                <a-textarea placeholder="Description" v-model="service.description" />
            </a-col>
            <a-col :span="8">
                    Paiement
                    <a-select default-value="Cash" size="large" v-model="service.payment">
                        <a-select-option value="cash">Cash</a-select-option>
                    </a-select>
            </a-col>
            <a-col :span="8">
                <label for="">Prix de base
                    <a-input type="number" placeholder="" addonAfter="Fcfa" v-model.number="service.base" />
                </label>
            </a-col>
            <a-col :span="8">
                <label>Prix Par Kilomètre
                    <a-input type="number" placeholder="" addonAfter="Fcfa" v-model.number="service.per_meter" />
                </label>
            </a-col>
            <a-col :span="8">
                <label >
                    Prix par durée
                    <a-input type="number" placeholder="" addonAfter="Fcfa" v-model.number="service.per_drive_time"/>
                </label>
            </a-col>
            <a-col :span="8">
                <label>
                    Prix par temps d'attente du conducteur
                    <a-input type="number"  addonAfter="Fcfa" v-model.number="service.per_waiting_time" />
                </label>
            </a-col>
            <a-col span="18" align="center" type="flex">
                <a-card>
                    <a-card-meta title="exemple d'estmation" description="équivalent d'une course cocody st-jean -- deux plateau"/>
                    <div class="mt-3 mb-4">
                        {{service.base}} + {{service.per_meter}} * 1 km + {{service.per_drive_time}} * 2 min + {{service.per_waiting_time}}
                    </div>
                </a-card>
            </a-col>
            <a-col :span="24">
                <a-button type="primary" class="right" @click="validate">Valider</a-button>
            </a-col>
            </a-row>
        
    </main>
</template>
<script>
import Axios from 'axios'

var service = {
    name: "",
    categorie_id: "",
    description: "",
    base: 100,
    per_meter: 0,
    per_drive_time: 0,
    per_waiting_time: 0,
    payment: "cash"
  }

export default {
    data(){
        return {
            service
        }
    },
    methods:{
        back: function(){
            //return back
            this.$router.go(-1)
        },
        validate:function () {
                if(this.$route.params.id){
                    Axios.post('http://localhost:8000/service/'+this.$route.params.id, this.service).then(response => {
                    this.$message.success('Service modifié avec succès')
                    this.$router.go('-1')
                }).catch(error => {
                    this.$message.error('Erreur lors de la modification du service'+error)
                })
            } else {
                Axios.post('http://localhost:8000/service/create', this.service).then(response => {
                    this.$message.success('Service ajouté avec succès')
                    this.$router.go('-1')
                }).catch(error => {
                    this.$message.error('Erreur lors de l\'ajout du service'+error)
                })
            }
        }
    },
    beforeMount: function(){
        if(this.$route.params.id){
            Axios.get("http://localhost:8000/service/"+this.$route.params.id).then(response => {
                this.service = response.data
            })
        }
    }
}

</script>