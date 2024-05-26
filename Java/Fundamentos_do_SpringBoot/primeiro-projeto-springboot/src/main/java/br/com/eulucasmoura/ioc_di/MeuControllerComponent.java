package br.com.eulucasmoura.ioc_di;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping
public class MeuControllerComponent {
    

    @Autowired
    MeuComponent meuComponent;

    @GetMapping("/component")
    public String chamandoComponent() {
        var resultado = meuComponent.chamarMeuComponent();
        return resultado;
    }
}
