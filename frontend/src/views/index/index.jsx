// This is the TODO page, where is rendering only the TODO component
import image from "../../../public/background2.jpg"; 
const IndexView = () => {

  return (
    <div>
      <div style={{textAlign:"center", padding:"200px", backgroundImage:`linear-gradient(rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.3)), url(${image})`, backgroundSize: 'cover', height:'100vh', }}>
        <h1 style={{color:"white", fontSize:"70px"}}>Directorio Médico Clínica Sta. María</h1>
        <br></br>
        <a style={{ fontSize:"25px"}}  href="/directory" active className="btn btn-secondary">Revisa Aquí</a>
      </div>
      <div>
      
      </div>
    </div>
  );
};

export default IndexView;