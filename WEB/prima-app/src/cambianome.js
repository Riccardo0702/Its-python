const CambiaNome = () =>{
    const [nome, setNome]=useState('Mario');
    const cambia = () =>{
        if (nome ==='Mario'){
            setNome('Riccardo')
        }else{
            setNome('Mario')
        }
    }
    return (<div>
        <h3>{nome}</h3>
        <button className='btn btn-dark' onClick={cambia}>Cambia Nome</button>
    </div>)
}

export default CambiaNome;