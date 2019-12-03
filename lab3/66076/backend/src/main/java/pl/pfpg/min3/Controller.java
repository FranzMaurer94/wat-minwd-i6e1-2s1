package pl.pfpg.min3;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import pl.pfpg.min3.model.InputRequest;
import pl.pfpg.min3.model.MainService;
import pl.pfpg.min3.model.UserInformation;
import pl.pfpg.min3.model.UserQueryResponse;

@RestController
@RequestMapping("/")
@Slf4j
@RequiredArgsConstructor

public class Controller {

  private final MainService mainService;

  @CrossOrigin
  @PostMapping("getUserData")
  public UserInformation getUserData(@RequestBody InputRequest input){
    return mainService.getUserData(input);
  }
}


