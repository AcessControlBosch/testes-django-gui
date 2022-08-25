export default {

    USER(state, payload){
        state.usuario = payload;
    },
    MACHINE(state, payload){
        state.idMachine = payload;
    },
    QNOTMARKEDSECURITY(state, payload){
        state.qNotMarkedSecurity = payload;
    },

    QNOTMARKEDSECURITY(state, payload){
        state.qNotMarkedSecurity = payload;
    },

    QNOTMARKEDENVIROMENT(state, payload){
        state.qNotMarkedEnviroment = payload;
    },

    IPMACHINE(state, payload){
        state.ipAddressMachine = payload;
    },
    IDMACHINE(state, payload){
        state.idmachine = payload;
    },

    MODALSECURITY(state, payload){
        state.modalSecurity = payload;
    },
    
    MODALENVIROMENT(state, payload){
        state.modalEnviroment = payload;
    }

}